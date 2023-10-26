import Image1 from "./Image1";

export default function ChocolateBox() {
    return (
        <div className="box">
            <Image1 />
            <div className="detail-box">
                <h6>
                    Yummy <span>chocolate</span>
                </h6>
                <h5>$5.0</h5>
                <a href="">BUY NOW</a>
            </div>
        </div>
    )
}