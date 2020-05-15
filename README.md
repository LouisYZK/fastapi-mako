# fastapi-mako
Mako templaye support for FastAPI

## Install 
```bash
pip install FastAPI-Mako
```

## Use

```python
from fastapi import FastAPI
from fastapi_mako import FastAPIMako

app = FastAPI()

app.__name__ = 'fast_blog' # Your application folder name

mako = FastAPIMako(app)

@app.get('/', response_class=HTMLResponse)
@mako.template('index.html')
def index(request: Request):
    setattr(request, 'mako', 'test')
    return {'title': 'Yurs'}

@app.get('/async_index', response_class=HTMLResponse)
@mako.template('index.html')
async def async_index(request: Request):
    setattr(request, 'mako', 'test')
    return {'title': 'Yurs'}
```

## Imeplement What?
Firt make mako search for the template path automiclly.

The wrap is just transmit the `app`, `request`, `context` in fastapi' application to the mako template and specify some exception and errors about mako template.