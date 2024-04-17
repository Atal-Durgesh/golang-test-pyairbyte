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
cache = ab.get_default_cache()
result = source.read(cache=cache,force_full_refresh=True)
prs=cache["pull_requests"].to_pandas()
prs.head(1)
print(prs)
