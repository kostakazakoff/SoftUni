class footballTeam {
    constructor(clubName, country) {
        this.clubName = clubName;
        this.country = country;
        this.invitedPlayers = [];
    }

    newAdditions(footballPlayers) {
        for (const p of footballPlayers) {
            const [name, age, playerValue] = p.split('/');
            if (!this.invitedPlayers.hasOwnProperty(name)) {
                this.invitedPlayers.push({ name, age, playerValue });
            } else if (this.invitedPlayers.playerValue < playerValue) {
                this.invitedPlayers.playerValue = playerValue;
            }
        }
        let output = [];
        for (const p of this.invitedPlayers) {
            output.push(p.name);
        }
        return `You successfully invite ${output.join(', ')}.`;
    }

    signContract(selectedPlayer) {
        const [name, offer] = selectedPlayer.split('/')
        const player = this.invitedPlayers.find(p => p.name === name);
        if (!player) {
            throw new Error(`${name} is not invited to the selection list!`);
        }
        if (typeof(player.playerValue) !== 'string' && offer < player.playerValue) {
            const priceDifference = player.playerValue - offer;
            throw new Error(`The manager's offer is not enough to sign a contract with ${name}, ${priceDifference} million more are needed to sign the contract!`)
        }
        player.playerValue = 'Bought';
        return `Congratulations! You sign a contract with ${name} for ${offer} million dollars.`;
    }

    ageLimit(name, age) {
        const player = this.invitedPlayers.find(p => p.name === name);
        if (!player) {throw new Error(`${name} is not invited to the selection list!`)};

        const ageDifference = age - player.age;
        if (ageDifference <= 0) {
            return `${name} is above age limit!`
        }else if (ageDifference < 5) {
            return `${name} will sign a contract for ${ageDifference} years with ${this.clubName} in ${this.country}!`;
        } else {
            return `${name} will sign a full 5 years contract for ${this.clubName} in ${this.country}!`;
        }
    }

    transferWindowResult() {
        const output = ['Players list:'];
        this.invitedPlayers.sort((a, b) => a.name.localeCompare(b.name))
        .forEach(p => {
            output.push(`Player ${p.name}-${p.playerValue}`);
        });
        return output.join('\n');
    }
}


let fTeam = new footballTeam("Barcelona", "Spain");
console.log(fTeam.newAdditions(["Pau Torres/25/52", "Kylian Mbappé/23/160", "Lionel Messi/35/50"]));
console.log(fTeam.signContract("Kylian Mbappé/240"));
console.log(fTeam.ageLimit("Kylian Mbappé", 30));
console.log(fTeam.transferWindowResult());
