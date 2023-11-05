/* eslint-disable react/prop-types */
const EstateCard = (props) => {
    const showDetailsClickHandler = (e) => {
        console.log(e)
    }


    return (
        <div className="card shadow" style={{ width: "18rem" }} key={props.id}>
            <img src="https://imageio.forbes.com/specials-images/imageserve/61cdd9ec2bbdedb659077751/Neutral-living-color-corrected/960x0.jpg?format=jpg&width=1440" className="card-img-top" alt="..." />
            <div className="card-body flex-column">
                <h5 className="card-title">
                    {props.name}
                </h5>
                <p className="card-text">
                    {props.description}
                </p>
                <div className="d-flex flex-column mb-3">
                    <div>
                        Rooms: {props.rooms}
                    </div>
                    <div>
                        Price: {props.price}
                    </div>
                </div>
                <button onClick={showDetailsClickHandler} className="btn btn-primary mt-auto">
                    Details
                </button>
            </div>
        </div>
    );
}

export default EstateCard