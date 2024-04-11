export type TypeDataField = {
    viewed_name: string,
    name: string,
    id?: number
}

export type TypePriceRange = {
    min_price: number,
    max_price: number
}

export type TypeFilterData = {
    gender: string[],
    category: string[],
    brand: string[],
    size: string[],
    color: string[],
    price: number,
    quantity: number,
    pageIndex: number,
    orderBy: string,
    basicCategory: string,
}
