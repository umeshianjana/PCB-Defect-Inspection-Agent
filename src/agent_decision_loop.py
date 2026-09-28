import json
from vision_inspector import PCBVisionInspector

class AgenticPCBController:
    """Agentic decision loop that dynamically acts on OpenCV perception output"""
    
    def process_inspection_results(self, inspection_data):
        total_defects = inspection_data.get("total_defects", 0)
        defects = inspection_data.get("defects", [])
        
        actions_taken = []
        
        if total_defects == 0:
            actions_taken.append({"action": "PASS_BOARD", "status": "APPROVED"})
        else:
            has_high_severity = any(d["severity"] == "HIGH" for d in defects)
            
            if has_high_severity:
                # Dynamic Tool Call 1: Trigger High-Res Rescan & Flag Critical Alert
                actions_taken.append({
                    "action": "TRIGGER_AWS_ALERT",
                    "target": "AWS_SNS_CRITICAL_QUEUE",
                    "reason": "High severity defect detected"
                })
                actions_taken.append({
                    "action": "HALT_CONVEYOR_LINE",
                    "target": "PLC_CONTROLLER",
                    "reason": "Immediate human review required"
                })
            else:
                # Dynamic Tool Call 2: Log to AWS DynamoDB telemetry
                actions_taken.append({
                    "action": "LOG_TO_DYNAMODB",
                    "target": "AWS_DYNAMODB_DEFECT_LOGS",
                    "reason": "Non-critical tracking telemetry"
                })
                
        return {
            "inspection_summary": inspection_data,
            "agent_actions": actions_taken
        }

if __name__ == "__main__":
    print("Agentic Decision Loop Engine Ready!")
