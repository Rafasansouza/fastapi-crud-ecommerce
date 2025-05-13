from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import create_product, get_products, get_product, delete_product, update_product

router = APIRouter()

# criar minha rota de buscar todos os itens
# sempre vai haver 2 itens obrigatorios, PATH e o meu RESPONSE
@router.get("/products/", response_model=List[ProductResponse])
def read_all_product(db: Session = Depends(get_db)):
    """
    esta e minha rota de ler todos os produtos da table products
    """
    products = get_products(db=db)
    return products

# criar minha rota de buscar 1 item
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id: int, db: Session = Depends(get_db)):
    """
    esta e minha rota de ler apenas 1 produto da table products
    """
    db_product = get_product(db=db,product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Voce esta buscando um produto que nao existe!")
    return db_product


# criar minha rota de adicionar um item
@router.post("/products/", response_model=ProductResponse)
def create_add_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    esta e minha rota para adicionar 1 produtos na table products
    """
    return create_product(db=db, product=product)

# criar minha rota de deletar um item
@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_one_product(product_id: int, db: Session = Depends(get_db)):
    """
    esta e minha rota para deletar um produto da table products
    """
    db_product = delete_product(product_id=product_id, db=db)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Voce esta deletando um produto que nao existe!")
    return db_product

# criar minha rota de fazer update nos itens
@router.put("/products/{product_id}", response_model=ProductResponse)
def update_one_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    """
    esta e minha rota para atualizar um produto da table products
    """
    product_db = update_product(db=db, product_id=product_id, product=product)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Voce esta tentando atualizar um produto que nao existe!")
    return product_db