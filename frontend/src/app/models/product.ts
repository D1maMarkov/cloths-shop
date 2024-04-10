import { TypeDataFilter } from "./filter"


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
    category: TypeDataFilter,
    color: string,
    sizes: string[],
    brand: TypeDataFilter,
    code: string,
    article: string,
}

export interface ICartProduct extends TypeBaseProduct {
    image: string,
    size: string,
    quantity: number
}
