/* eslint-disable react/prop-types */
const EstateCard = (props) => {
    return (
        <div className="card" style={{ width: "18rem" }} key={props.id}>
            {/* <img src="..." className="card-img-top" alt="..." /> */}
            <div className="card-body">
                <h5 className="card-title">{props.name}</h5>
                <p className="card-text">
                    {props.description}
                </p>
                <a href="#" className="btn btn-primary">
                    Details
                </a>
            </div>
        </div>
    );
}

export default EstateCard