function solve(n, ...operations) {
    operations.forEach(operation => {
        switch (operation) {
            case 'chop':
                n /= 2;
                console.log(n)
                break;
            case 'dice':
                n = Math.sqrt(n);
                console.log(n)
                break;
            case 'spice':
                n++;
                console.log(n)
                break;
            case 'bake':
                n *= 3;
                console.log(n)
                break;
            case 'fillet':
                n -= n * 0.2;
                console.log(n)
                break;
        }
    })
}
