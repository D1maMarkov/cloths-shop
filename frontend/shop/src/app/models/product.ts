import { TypeDataFilter } from "./filter"


export interface IProduct {
    id: number,
    name: string,
    description: string,
    price: number,
    images: string[],
    gender: string,
    category_id: number,
    category: TypeDataFilter,
    color_id: number,
    color: string,
    sizes: string[]
    brand_id: number,
    brand: TypeDataFilter,
    code: string,
    article: string,
    basic_category: string
    created: string
}

export type TypeCartProduct = {
    id: number,
    name: string,
    description: string,
    price: number,
    image: string,
    size: string,
    quantity: number
}