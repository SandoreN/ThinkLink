from app import app

if __name__ == '__main__':
    # Print all registered routes to help debug 404 errors
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} -> {rule.endpoint}")

    # Run the Flask application on port 8080
    app.run(host='0.0.0.0', port=8080)
