import os
import sys
import json

def load_config(config_path):
    """Load the configuration from a JSON file."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def replace_placeholders(config, template_path, output_path):
    """Replace placeholders in the template file with values from the config and save to output."""
    with open(template_path, 'r') as template_file:
        content = template_file.read()

    # Replace each placeholder in the template with the corresponding config value
    for key, value in config.items():
        placeholder = f"<{key}>"  # Placeholder format
        content = content.replace(placeholder, str(value))

    # Write the processed content to the output file
    with open(output_path, 'w') as output_file:
        output_file.write(content)
    print(f"Processed template saved to {output_path}")

if __name__ == "__main__":
    # Check if a config path argument is provided, otherwise default to 'config.json' in the script directory
    config_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), 'config.json')

    try:
        
        # create nginx folder
        nginx_folder = "nginx"
        os.makedirs(nginx_folder, exist_ok=True)
        
        # Load configuration
        config = load_config(config_path)

        # Replace placeholders in the template files
        replace_placeholders(config, 'templates/test_server.py.template', 'test/test_server.py')
        replace_placeholders(config, 'templates/nginx.conf.template', 'nginx/nginx.conf')
        replace_placeholders(config, 'templates/Dockerfile.nginx.template', 'nginx/Dockerfile')
        replace_placeholders(config, 'templates/docker-compose.yml.template', './docker-compose.yml')

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
