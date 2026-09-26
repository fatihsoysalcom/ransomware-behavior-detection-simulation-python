import os
import shutil
import tempfile
import time
import random

def create_dummy_files(directory, count=10):
    """Creates dummy text files in the specified directory."""
    os.makedirs(directory, exist_ok=True)
    print(f"Creating {count} dummy files in '{directory}'...")
    for i in range(count):
        filename = os.path.join(directory, f"document_{i}.txt")
        with open(filename, 'w') as f:
            f.write(f"This is a test document number {i}. It contains some important data.\n")
            f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n" * 5)
        print(f"  Created: {os.path.basename(filename)}")
    print("Dummy files created.")

def simulate_ransomware_attack(directory, new_extension=".locked", delay_per_file=0.05):
    """Simulates a ransomware attack by 'encrypting' and renaming files."""
    print(f"\nSimulating ransomware attack in '{directory}'...")
    files_to_encrypt = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".txt")]
    
    if not files_to_encrypt:
        print("No .txt files found to 'encrypt'.")
        return

    for filepath in files_to_encrypt:
        try:
            # Simulate 'encryption' by overwriting content with random bytes.
            # In a real ransomware, this would be actual cryptographic encryption.
            # Here, we just corrupt the file to show it's modified.
            with open(filepath, 'rb+') as f:
                original_size = os.fstat(f.fileno()).st_size
                f.seek(0)
                f.write(os.urandom(original_size)) # Overwrite with random bytes
                f.truncate(original_size) # Keep original size
            
            # Simulate file renaming, a common ransomware tactic.
            new_filepath = filepath + new_extension
            os.rename(filepath, new_filepath)
            print(f"  'Corrupted' and renamed: {os.path.basename(filepath)} -> {os.path.basename(new_filepath)}")
            time.sleep(delay_per_file) # Simulate some processing time
        except Exception as e:
            print(f"  Error processing {filepath}: {e}")
    print("Ransomware simulation finished.")

def detect_ransomware_activity(directory, suspicious_extension=".locked", detection_threshold=10):
    """
    Detects potential ransomware activity by looking for a sudden surge of
    files with a suspicious extension.
    
    The article discusses ETW (Windows) and eBPF (Linux) for deep system
    monitoring. These tools would provide real-time events like:
    - File creation, modification, deletion, renaming.
    - Process activity (which process is performing these actions).
    
    This simulation demonstrates a high-level detection heuristic based on
    the *outcome* of such events: a large number of files rapidly acquiring
    a new, unknown extension. A real ETW/eBPF-based detector would analyze
    the *sequence* and *volume* of these events in real-time.
    """
    print(f"\nDetecting ransomware activity in '{directory}'...")
    suspicious_files = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(suspicious_extension):
                suspicious_files.append(os.path.join(root, filename))
    
    num_suspicious_files = len(suspicious_files)
    print(f"  Found {num_suspicious_files} files with extension '{suspicious_extension}'.")

    if num_suspicious_files >= detection_threshold:
        print(f"  !!! ALERT: High number of suspicious files detected ({num_suspicious_files}).")
        print("  This pattern (rapid file modification and renaming with a new extension)")
        print("  is characteristic of ransomware behavior.")
        print("  Affected files:")
        for f in suspicious_files:
            print(f"    - {os.path.basename(f)}")
        return True
    else:
        print("  No significant ransomware activity detected based on file extensions.")
        return False

def main():
    temp_dir = None
    try:
        temp_dir = tempfile.mkdtemp(prefix="ransomware_test_")
        print(f"Working in temporary directory: {temp_dir}")

        create_dummy_files(temp_dir, count=15)

        ransom_extension = ".encrypted_by_evil_hacker" # Use a distinct extension for detection
        simulate_ransomware_attack(temp_dir, new_extension=ransom_extension, delay_per_file=0.05)
        
        detect_ransomware_activity(temp_dir, suspicious_extension=ransom_extension, detection_threshold=10)

    finally:
        if temp_dir and os.path.exists(temp_dir):
            print(f"\nCleaning up temporary directory: {temp_dir}")
            shutil.rmtree(temp_dir)
            print("Cleanup complete.")

if __name__ == "__main__":
    main()
