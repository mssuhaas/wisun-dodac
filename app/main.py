from pydbus import SystemBus
import base64
from fastapi import FastAPI

def base64_to_hex(base64_bytes):
    """
    Convert bytes to a hexadecimal string.
    """
    try:
        hex_string = base64_bytes.hex()
        # Insert ":" after every two characters
        mac_with_colons = ":".join([hex_string[i:i+2] for i in range(0, len(hex_string), 2)])
        return mac_with_colons
    except Exception as e:
        print(f"Error converting bytes to hex: {e}")
        return None

def get_valid_edges():
    """
    Retrieves the valid edges from the nodes data.

    Returns:
        dict: A dictionary containing the valid edges in the form of a tree.
              The keys are 'tree' and the values are lists of valid edges.
    """
    valid_edges = []
    try:
        border_router_eui64 = None
        nodes_data = proxy.Nodes
        for node in nodes_data:
            eui64_bytes = bytes(node[0])
            node_info = node[1]
            if len(node_info['ipv6']) == 2 and node_info['node_role'] == NODE_ROLES['BorderRouter']:
                border_router_eui64 = base64_to_hex(eui64_bytes)
                break

        # Collect valid edges
        for node in nodes_data:
            eui64_bytes = bytes(node[0])
            node_info = node[1]
            if len(node_info['ipv6']) == 2:
                if 'parent' in node_info and node_info['parent'] is not None:
                    parent_eui64 = base64_to_hex(bytes(node_info['parent']))
                elif node_info['node_role'] == NODE_ROLES['LFN']:
                    parent_eui64 = border_router_eui64
                else:
                    parent_eui64 = None

                eui64 = base64_to_hex(eui64_bytes)
                if parent_eui64:
                    valid_edges.append([eui64, parent_eui64])

        return {"tree": valid_edges}

    except Exception as e:
        print(f"Exception occurred: {e}")
        return []

# Constants
NODE_ROLES = {
    'BorderRouter': 0,
    'FFN': 1,
    'LFN': 2
}

app = FastAPI()
bus = SystemBus()
proxy = bus.get("com.silabs.Wisun.BorderRouter")

@app.get("/")
async def read_valid_edges():
    return get_valid_edges()
    
