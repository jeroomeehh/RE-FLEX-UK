import requests
import random

def get_latest_user_agent():
    """
    Fetches a list of modern Android User-Agents from a public source
    and returns a random one.
    """
    try:
        # This URL points to a frequently updated list of User-Agents
        url = "https://raw.githubusercontent.com/Lumo93/RE-FLEX-UK/main/useragentlist"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)

        user_agents = [line.strip() for line in response.text.splitlines() if line.strip()]
        if not user_agents:
            raise ValueError("No User-Agents found in the fetched list.")

        return random.choice(user_agents)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching User-Agent list: {e}")
        # Fallback to a known-good, modern User-Agent if the fetch fails
        return "Dalvik/2.1.0 (Linux; U; Android 13; SM-S908U Build/TP1A.220624.014)"

if __name__ == '__main__':
    # You can run this file directly to test it
    print(get_latest_user_agent())