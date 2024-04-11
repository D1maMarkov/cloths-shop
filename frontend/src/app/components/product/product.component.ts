import { ICatalogProduct } from "src/app/models/product";
import { Component, Input } from "@angular/core";
import { Router } from "@angular/router";
import { fadeIn } from "src/app/animations/fade-in.animation";

@Component({
    selector: "catalog-product",
    templateUrl: "./product.component.html",
    styleUrls: ["./product.component.scss"],
    animations: [fadeIn],
})
export class ProductComponent{
    hover = false;
    @Input() product: ICatalogProduct;

    constructor(
        private route: Router
    ){}

    async goToProductPage(){
        await this.route.navigate(["product/" + this.product.id])
    }
}
