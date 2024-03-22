export const novelsImages = [
    {image: "rick.png", height: 150, title:"Rick Owens"},
    {image: "ad2.jpg", height: 190, title:"Adidas"},
    {image: "9ad.png", height: 190, title:"Adidas"},
    {image: "defender.png", height: 150, title:"Balenciaga"},
    {image: "Viperr1.png", height: 150, title:"Viperr"},
    {image: "9rick.png", height: 190, title:"Rick Owens"}
];

export const brandsImages = [
    {image: "defender.png", height: 150, title: "Balenciaga"},
    {image: "vetements.png", height: 190, title:"Vetements"},
    {image: "balenci-kai.png", height: 190, title:"Balenciaga"},
    {image: "rick.png", height: 150, title:"Rick Owens"},
    {image: "balenci_black.png", height: 150, title:"Balenciaga"},
    {image: "kai-rick.png", height: 190, title:"Rick Owens"}
];

export const male = [
    {image: "Viperr1.png", height: 150, title: "Viperr"},
    {image: "9ad.png", height: 190, title: "Adidas"},
    {image: "kai-rick.png", height: 190, title: "Rick Owens"},
    {image: "rp3.webp", height: 150, title: "Rick Owens"},
    {image: "balenci_white.png", height: 150, title:"Balenciaga"},
    {image: "vet.png", height: 190, title: "Vetements"}
]

export const female = [
    {image: "rp3.webp", height: 150, title: "Rick Owens"},
    {image: "kai-rick.png", height: 190, title: "Rick Owens"},
    {image: "t.jpg", height: 190, title: "Rick Owens"},
    {image: "defender.png", height: 150, title: "Balenciaga"},
    {image: "newrocki.png", height: 150, title:"Newrocki"},
    {image: "9ad.png", height: 190, title: "Adidas"}
]

export const accessories = [
    {image: "gv.jpg", height: 150, title: "Givenchy"},
    {image: "rc3.png", height: 190, title: "Rick Owens"},
    {image: "vetements.png", height: 190, title: "Vetements"},
    {image: "Viperr1.png", height: 150, title: "Viperr"},
    {image: "rick3.png", height: 150, title: "Rick Owens"},
    {image: "ad2.jpg", height: 190, title: "Adidas"}
]

type TypeLabel = {
    title: string,
    slug: string,
}

export const labels: TypeLabel[] = [
    {title: "Новинки", slug: "new"}, 
    {title: "Бренды", slug: "brands"},
    {title: "Мужское", slug: "muzhskoe"},
    {title: "Женское", slug: "zhenskoe"},
    {title: "Аксессуары", slug: "accessories"}
];