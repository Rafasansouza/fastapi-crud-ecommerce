from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel

#get all (select * from)
def get_products(db: Session):
    """
    essa funcao retorna todos os produtos da table product
    """
    return db.query(ProductModel).all()

#get where id = 1
def get_product(db: Session, product_id: int):
    """
    essa funcao retorna apenas um produto da table product
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

#insert into (create)
def create_product(db: Session, product: ProductCreate):
    """
    essa funcao insere um registro na table product
    """
    #transformar minha view para ORM
    db_product = ProductModel(**product.model_dump())
    #adicionar na table
    db.add(db_product)
    #commitar na table
    db.commit()
    #fazer refresh do db
    db.refresh(db_product)
    #retornar para o user o item criado
    return db_product

#update where id = 1
def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    
    if db_product is None:
        return None
    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.category is not None:
        db_product.category = product.category
    if product.email_supplier is not None:
        db_product.email_supplier = product.email_supplier
    db.commit()
    db.refresh(db_product)
    return db_product
    

#delete where id = 1
def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product