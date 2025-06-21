import subprocess


def get_ollama_names():
    try:
        # Run the shell command 'ollama list' and capture its output as text
        result = subprocess.run(
            ["ollama", "list"],  # Command and arguments as a list
            capture_output=True,  # Capture standard output and error
            text=True,  # Decode output as string instead of bytes
            check=True,  # Raise exception if command returns non-zero exit code
        )

        # Split the output into lines and remove any leading/trailing whitespace
        lines = result.stdout.strip().split("\n")

        # Skip the header line, extract the first word (name) from each remaining line
        names = [line.split()[0] for line in lines[1:]]

        # Return the list of extracted names
        return names

    except subprocess.CalledProcessError as e:
        # Handle cases where the command fails (non-zero exit code)
        print(f"Command failed with exit code {e.returncode}")
        print(e.output)

    except FileNotFoundError:
        # Handle case when 'ollama' command is not found (not installed or not in PATH)
        print(
            "Error: 'ollama' command not found. Please ensure Ollama is installed and in your PATH."
        )

    # Return empty list if an error occurs
    return []


# if __name__ == "__main__":
#     print(get_ollama_names())
