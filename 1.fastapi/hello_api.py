from fastapi import FastAPI


app = FastAPI(title="Hello API")


# GET, POST, PATCH, DELETE, UPDATE, OPTIONS
@app.get("/")
def root(nombre: str | None = None):
    return {"message": f"hello {nombre if nombre is not None else 'amigo'}", "status": "OK"}


def main():
    """Main function"""
    import uvicorn

    uvicorn.run("hello_api:app", reload=True)


if __name__ == "__main__":
    # only run this if the file is executed as a script
    main()