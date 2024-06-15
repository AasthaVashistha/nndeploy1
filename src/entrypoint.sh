#!/bin/bash

# Run the training script
python3 /app/src/train_pipeline.py

# Check if the model was created successfully
if [ -f /app/src/trained_models/two_input_xor_nn.pkl ]; then
    # Run the prediction script
    python3 /app/src/predict.py
else
    echo "Model file not found!"
    exit 1
fi

# Keep the container running indefinitely
tail -f /dev/null

