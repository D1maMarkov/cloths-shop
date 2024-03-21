from schemas.common import SBaseDataField
from schemas.products import SProduct
from settings import Settings


def serialize_brand(brand) -> SBaseDataField:
    brand = brand.__dict__
    brand["viewed_name"] = brand["name"]
    
    brand = SBaseDataField(**brand)
    
    return brand

def full_serialize_product(product) -> SProduct:
    product = product.__dict__
    product["images"] = [f'{Settings.HOST}/products/image/{image.id}' for image in product["images"]]
    
    product["category"] = product["category"].__dict__
    product["brand"] = serialize_brand(product["brand"])
    product["sizes"] = [size.size for size in product["sizes"]]
    if not product["sizes"]:
        product["sizes"] = ["ONE SIZE"]
        
    product["color"] = product["color"].__dict__
 
    product = SProduct(**product)
    
    return product