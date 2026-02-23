"""
Simple API Test Script for WellTrack
Tests all endpoints to verify functionality
"""
import requests


BASE_URL = "http://localhost:5000/api"


def test_register():
    print("\n1. Testing Registration...")
    response = requests.post(
        f"{BASE_URL}/register",
        json={"username": "testuser", "password": "testpass"}
    )
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    return response.status_code == 201


def test_login():
    print("\n2. Testing Login...")
    response = requests.post(
        f"{BASE_URL}/login",
        json={"username": "testuser", "password": "testpass"}
    )
    print(f"   Status: {response.status_code}")
    data = response.json()
    print(f"   Response: {data}")
    return data.get('token') if response.status_code == 200 else None


def test_log_mood(token):
    print("\n3. Testing Mood Logging...")
    response = requests.post(
        f"{BASE_URL}/mood",
        headers={"Authorization": token},
        json={
            "mood_level": 4,
            "mood_tags": "happy, productive",
            "notes": "Had a great day!"
        }
    )
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    return response.status_code == 201


def test_mood_history(token):
    print("\n4. Testing Mood History...")
    response = requests.get(
        f"{BASE_URL}/mood/history",
        headers={"Authorization": token}
    )
    print(f"   Status: {response.status_code}")
    data = response.json()
    print(f"   Entries found: {len(data.get('entries', []))}")
    if data.get('entries'):
        print(f"   Latest entry: {data['entries'][0]}")
    return response.status_code == 200


def run_tests():
    print("=" * 50)
    print("WellTrack API Test Suite")
    print("=" * 50)
    print("\nMake sure the backend server is running!")
    print("Run: python backend/app.py")
    input("\nPress Enter to start tests...")

    # Test registration
    test_register()

    # Test login and get token
    token = test_login()
    if not token:
        print("\n❌ Login failed. Cannot continue tests.")
        return

    # Test mood logging
    test_log_mood(token)

    # Test mood history
    test_mood_history(token)

    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
