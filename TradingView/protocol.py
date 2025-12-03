
import json

class Protocol:
    @staticmethod
    def parse_ws_packet(packet: str) -> list:
        """Parse WebSocket packet"""
        results = []
        
        # Handle ping packets
        if packet.startswith('~h~'):
            try:
                results.append(int(packet[3:]))
            except ValueError:
                pass
            return results

        # Handle normal packets
        if '~m~' in packet:
            packets = packet.split('~m~')
            for i in range(1, len(packets), 2):
                try:
                    payload_len = int(packets[i])
                    payload_str = packets[i+1]
                    if payload_len == len(payload_str):
                        results.append(json.loads(payload_str))
                except (ValueError, json.JSONDecodeError):
                    continue

        return results

    @staticmethod
    def format_ws_packet(packet: any) -> str:
        """Format WebSocket packet"""
        if isinstance(packet, str):
            return packet
        
        if isinstance(packet, dict):
            message = json.dumps(packet, separators=(',', ':')).replace('null', '""')
            return f"~m~{len(message)}~m~{message}"
        
        return str(packet)
