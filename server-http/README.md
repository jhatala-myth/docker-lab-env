```bash
DOCKER_BUILDKIT=1 docker image build --no-cache  --network host --force-rm -t $(basename $(pwd) | tr '[:upper:]' '[:lower:]') -f Dockerfile .
```