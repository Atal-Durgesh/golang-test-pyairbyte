import airbyte as ab

# Create and configure the source:
source = ab.get_source(
    "source-github",
    install_if_missing=True,
    config={
        "repositories": ["Atal-Durgesh/SpringSecurity"],
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
print(result.streams().items())
