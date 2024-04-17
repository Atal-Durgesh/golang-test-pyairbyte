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
print(result.to_pandas())
