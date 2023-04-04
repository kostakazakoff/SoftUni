class Triathlon {
    constructor(competitionName) {
        this.competitionName = competitionName;
        this.participants = {};
        this.listOfFinalists = [];
    }

    addParticipant(participantName, participantGender) {
        if (this.participants.hasOwnProperty(participantName)) {
            return `${participantName} has already been added to the list`;
        }
        this.participants[participantName] = participantGender;
        return `A new participant has been added - ${participantName}`;
    }

    completeness(participantName, condition) {
        if (!this.participants.hasOwnProperty(participantName)) {
            throw new Error(`${participantName} is not in the current participants list`);
        }
        const completedCount = Math.floor(condition / 30);
        if (condition < 30) {
            throw new Error(`${participantName} is not well prepared and cannot finish any discipline`)
        }
        if (completedCount < 3) {
            return `${participantName} could only complete ${completedCount} of the disciplines`;
        }
        const gender = this.participants[participantName];
        this.listOfFinalists.push({ participantName, gender });
        delete this.participants[participantName];

        return `Congratulations, ${participantName} finished the whole competition`;
    }

    rewarding(participantName) {
        const existInFinalists = this.listOfFinalists.find(f => f.participantName === participantName);
        if (!existInFinalists) { return `${participantName} is not in the current finalists list` };

        return `${participantName} was rewarded with a trophy for his performance`;
    }

    showRecord (criteria) {
        if (this.listOfFinalists.length === 0) {return `There are no finalists in this competition`};
        const searchBy = {
            'all': '',
            'male': 'male',
            'female': 'female'
        }

        if (criteria !== 'all') {
            const finalist = this.listOfFinalists.find(f => Object.values(f).includes(searchBy[criteria]));
            const first = finalist.participantName;
            return `${first} is the first ${criteria} that finished the ${this.competitionName} triathlon`;
        }

        const output = [`List of all ${this.competitionName} finalists:`];
        const sortedFinalists = this.listOfFinalists.map(f => f.participantName)
        .sort((a, b) => a.localeCompare(b));
        sortedFinalists.forEach(f => output.push(f));
        return output.join('\n');
    }
}


// const contest = new Triathlon("Dynamos");
// console.log(contest.addParticipant("Peter", "male"));
// console.log(contest.addParticipant("Sasha", "female"));
// console.log(contest.completeness("Peter", 100));
// console.log(contest.completeness("Sasha", 90));
// console.log(contest.rewarding("Peter"));
// console.log(contest.rewarding("Sasha"));
// console.log(contest.showRecord("all"));
