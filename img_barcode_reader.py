import torch
import cv2
import os
import json
import asyncio
import websockets
import time
from pyzbar import pyzbar

# Define paths
INPUT_FOLDER = "/home/shake/snapshots"
OUTPUT_FOLDER = "/home/shake/snapshots_output"
BACKEND_WS_URL = "ws://localhost:8765?client_id=yoloscanner"  # Replace with your actual WebSocket backend

# Ensure output directory exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load YOLO model
device = torch.device("cpu")
model = torch.hub.load("ultralytics/yolov5", "custom", path="model.pt").to(device)

# Store already processed images to prevent reprocessing
processed_images = set()


async def process_images():
    async with websockets.connect(BACKEND_WS_URL) as websocket:
        print("Connected to WebSocket Backend!")

        while True:  # Infinite loop to keep checking for new images
            images = os.listdir(INPUT_FOLDER)

            for image_file in images:
                image_path = os.path.join(INPUT_FOLDER, image_file)

                # Skip already processed images
                if image_file in processed_images:
                    continue

                frame = cv2.imread(image_path)
                if frame is None:
                    print(f"Skipping invalid image: {image_file}")
                    continue

                results = model(frame)
                detections = results.pandas().xyxy[0]

                detected_barcodes = []

                # Process detected objects
                for i, detection in detections.iterrows():
                    x1, y1, x2, y2 = map(int, detection[['xmin', 'ymin', 'xmax', 'ymax']])

                    class_id = detection["class"]
                    confidence = detection["confidence"]
                    print(f"Processing {image_file} - Detection {i}: class {class_id}, confidence {confidence:.2f}")

                    # Draw bounding box on image
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    # Crop and convert to grayscale
                    cropped_img = frame[y1:y2, x1:x2]
                    gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
                    barcodes = pyzbar.decode(gray)

                    # Process detected barcodes
                    for barcode in barcodes:
                        barcode_data = barcode.data.decode("utf-8")
                        detected_barcodes.append({"barcode": barcode_data, "bbox": [x1, y1, x2, y2]})
                        print(f"Detected barcode: {barcode_data}")

                        # Put barcode data on image
                        cv2.putText(frame, barcode_data, (x1, y2 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

                # Save processed image
                output_path = os.path.join(OUTPUT_FOLDER, image_file)
                cv2.imwrite(output_path, frame)

                # Store results in JSON format
                image_result = {
                    "image": image_file,
                    "barcodes": detected_barcodes
                }

                # Send the result to the backend WebSocket
                if detected_barcodes:
                    json_data = json.dumps(image_result)
                    await websocket.send(json_data)
                    print(f"Sent to WebSocket: {json_data}")

                # Mark image as processed
                processed_images.add(image_file)

            print("Waiting for new images...")
            await asyncio.sleep(3)  # Wait 3 seconds before checking for new images


# Run the WebSocket process continuously
asyncio.run(process_images())
