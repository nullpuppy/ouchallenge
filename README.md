# OfferUp Backend Coding Challenge

Super simple micropservice for retrieving price recommendations for a given item in a given city.

## Requirements

Uses Django and Django Rest Framework.

Targetting vagrant with Ubuntu 14.04 with 1 CPU and 1024MB RAM.

## Usage

> git clone https://github.com/nullpuppy/ouchallenge
> cd ouchallenge
> vagrant up
> vagrant ssh
> uwsgi --ini ouchallenge/owsgi-vagrant.ini

## API

| Endpoint | Description |
| -------- | ----------- |
| GET /item-price-service/?item=&city=   | Retrieve Pricing recommendation based on item and city |

## Example

GET /item-price-service/?item=Furniture&city=Philadelphia

```json
{
    "status": 200,
    "content": {
        "item": "Furniture",
        "item_count": 6,
        "price_suggestion": 33,
        "city": "Philadelphia"
   }
}
```

GET /item-price-service/?item=Furniture

```json
{
    "status": 200,
    "content": {
        "item": "Furniture",
        "item_count": 6,
        "price_suggestion": 33,
        "city": "Not Specified"
   }
}
```

GET /item-price-service/

```json
{
    "status": 404,
    "content": {
        "message": "Not Found",
   }
}
```


