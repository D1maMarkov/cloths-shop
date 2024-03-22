import { transition, style, animate, trigger } from "@angular/animations";
import { IProduct } from "src/app/models/product";
import { Component, Input } from "@angular/core";
import { Router } from "@angular/router";

const enterTransition = transition(":enter", [
    style({
        opacity: 0,
        height: 0
    }),
    animate('.15s ease-in', style({opacity: 1, height: "*"})),
]);
const fadeIn = trigger('fadeIn', [enterTransition]);

@Component({
    selector: "catalog-product",
    templateUrl: "./product.component.html",
    styleUrls: ["./product.component.scss"],
    animations: [fadeIn],
})
export class ProductComponent{
    hover = false;
    @Input() product: IProduct;

    constructor(
        private route: Router
    ){}

    async goToProductPage(){
        await this.route.navigate(["product/" + this.product.id])
    }
}