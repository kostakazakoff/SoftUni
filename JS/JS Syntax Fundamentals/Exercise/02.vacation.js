function vacation(groupQuantity, typeOfGroup, dayOfWeek){
    let ticketPrice;
    let totalPrice;
    switch(typeOfGroup){
        case 'Students':
            switch(dayOfWeek){
                case 'Friday':
                    ticketPrice = 8.45
                    break;
                case 'Saturday':
                    ticketPrice = 9.80
                    break;
                case 'Sunday':
                    ticketPrice = 10.46
                    break;
            }
            totalPrice = groupQuantity * ticketPrice
            if (groupQuantity >= 30){
                totalPrice *= 0.85;
            }
            break;
        case 'Business':
            switch(dayOfWeek){
                case 'Friday':
                    ticketPrice = 10.90
                    break;
                case 'Saturday':
                    ticketPrice = 15.60
                    break;
                case 'Sunday':
                    ticketPrice = 16
                    break;
            }
            if (groupQuantity >= 100){
                groupQuantity -= 10;
            }
            totalPrice = groupQuantity * ticketPrice
            break;
        case 'Regular':
            switch(dayOfWeek){
                case 'Friday':
                    ticketPrice = 15
                    break;
                case 'Saturday':
                    ticketPrice = 20
                    break;
                case 'Sunday':
                    ticketPrice = 22.50
                    break;
            }
            totalPrice = groupQuantity * ticketPrice
            if (groupQuantity >= 10 && groupQuantity <= 20){
                totalPrice *= 0.95
            }
            break;
    }
    console.log(`Total price: ${totalPrice.toFixed(2)}`)
}