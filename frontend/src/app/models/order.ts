import { ICartProduct } from "./product";

export type TypeOrder = {
    created: string,
    status: string,
    order_products: ICartProduct[],
}

export type TypeCreateOrder = {
    name: string | null | undefined,
    secondname: string | null | undefined,
    delivery: string | null | undefined,
    payment: string | null | undefined,
    adress: string | null | undefined,
    phone: string | null | undefined,
}
