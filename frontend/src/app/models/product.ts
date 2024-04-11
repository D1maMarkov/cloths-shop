import { TypeDataField } from "./filter"


export type TypeBaseProduct = {
    id: number,
    name: string,
    description: string,
    price: number,
}

export interface ICatalogProduct extends TypeBaseProduct {
    image: string,
    sizes: string[]
}

export interface IProduct extends TypeBaseProduct {
    images: string[],
    gender: string,
    category: TypeDataField,
    color: string,
    sizes: string[],
    brand: TypeDataField,
    code: string,
    article: string,
}

export interface ICartProduct extends TypeBaseProduct {
    image: string,
    size: string,
    quantity: number
}
