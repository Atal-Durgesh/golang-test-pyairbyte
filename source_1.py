import airbyte as ab

# Create and configure the source:
source = ab.get_source(
    "source-github",
    install_if_missing=True,
    config={
        "repositories": ["Atal-Durgesh/golang-test-pyairbyte"],
        "credentials": {
            "personal_access_token": "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",
        },
    },
)

# Verify the config and creds by running `check`:
source.check()
source.get_available_streams()
source.select_streams(["pull_requests"])
result = source.read()
print(result.to_pandas())
