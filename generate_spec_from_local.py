import json
import sys
from pathlib import Path
import argparse

from fastapi.openapi.utils import get_openapi


def main(repo_path_str: str, output_file_str: str):
    """
    Generates the OpenAPI spec from a local repository path and saves it
    to a specified output file.
    """
    repo_path = Path(repo_path_str).resolve()
    output_file = Path(output_file_str)

    print(f"--- 🐍 Generating spec from local path: {repo_path} ---")

    if not repo_path.is_dir():
        print(f"❌ ERROR: Provided repository path not found at '{repo_path}'")
        sys.exit(1)

    # Ensure the destination directory for the output file exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    repo_path_str_resolved = str(repo_path)
    try:
        sys.path.insert(0, repo_path_str_resolved)

        # Set SERVICE_ROOT_PATH to empty string to disable root_app mounting
        # This ensures we get the main app with all routes for OpenAPI spec generation
        import os
        os.environ["SERVICE_ROOT_PATH"] = ""

        print("🔍 Importing FastAPI app factory 'create_application'...")
        from src.main import create_application

        print("🛠️ Creating FastAPI app instance from factory...")
        app = create_application()

        print("🔩 Generating OpenAPI schema in memory...")
        openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        )

        print(f"💾 Saving schema to '{output_file}'...")
        with open(output_file, "w") as f:
            json.dump(openapi_schema, f, indent=2)

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        raise
    finally:
        if repo_path_str_resolved in sys.path:
            sys.path.remove(repo_path_str_resolved)

    print("\n✅ --- Python script finished successfully! ---")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate OpenAPI spec from a local FastAPI repository."
    )
    # Argument 1: The path to the repo to analyze
    parser.add_argument(
        "repo_path",
        type=str,
        help="The path to the local repository clone."
    )
    # Argument 2: The path where the final JSON file should be saved
    parser.add_argument(
        "--output",
        required=True,
        type=str,
        help="Path to save the generated openapi.json file."
    )
    args = parser.parse_args()
    main(args.repo_path, args.output)