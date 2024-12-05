# RanobeDays

Website for reading novels online, upload your own works or upload translated existing novels from other languages.

## Development

1. Clone repo
```bash
git clone https://github.com/demindx/RanobeDays
```

2. cd to directory

```bash
cd RanobeDays/backend
```

3. create .env file and set environment variables as shown in .env.example file

4. generate secret key and copy it to .env file

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

5. Run docker compose build

```bash
docker compose build
```

6. Run backend server

```bash
docker compose up
```

## Api docs
Api docs are available at http://localhost:8000/api/v1/documentation/
