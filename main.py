import cv2
import numpy as np
import json
from src.vision_inspector import PCBVisionInspector
from src.agent_decision_loop import AgenticPCBController

def create_synthetic_pcb_image(has_defect=True):
    """Generates a synthetic PCB image for demonstration and testing"""
    # Create a green circuit board background
    img = np.zeros((400, 600, 3), dtype=np.uint8)
    img[:] = (34, 139, 34)  # PCB Green
    
    # Draw copper tracks and pads
    cv2.rectangle(img, (50, 100), (550, 120), (0, 215, 255), -1)
    cv2.circle(img, (150, 200), 25, (0, 215, 255), -1)
    cv2.circle(img, (450, 200), 25, (0, 215, 255), -1)
    
    if has_defect:
        # Simulate a major solder bridge / short circuit defect
        cv2.rectangle(img, (140, 110), (160, 185), (0, 255, 255), -1)
        
    return img

def run_pipeline():
    print("==================================================")
    print("🚀 Running PCB Defect Inspection Agentic Pipeline")
    print("==================================================\n")
    
    # 1. Simulate Image Capture
    sample_image = create_synthetic_pcb_image(has_defect=True)
    
    # 2. Vision Perception Stage (OpenCV 5)
    inspector = PCBVisionInspector()
    inspection_results = inspector.inspect_defects(sample_image)
    
    print("🔍 Perception Layer Output (OpenCV 5):")
    print(json.dumps(inspection_results, indent=2))
    
    # 3. Agentic Decision & Control Loop
    agent = AgenticPCBController()
    final_execution = agent.process_inspection_results(inspection_results)
    
    print("\n🧠 Agentic Decision Loop Execution Result:")
    print(json.dumps(final_execution, indent=2))

if __name__ == "__main__":
    run_pipeline()
