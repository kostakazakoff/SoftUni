function browserHistory(history, actions) {
    actions.forEach(element => {
        let [action, soft] = element.split(' ');
        if (action === 'Open' && !history['Open Tabs'].includes(soft)) {
            history['Open Tabs'].push(soft);
            history['Browser Logs'].push(element);
        } else if (action === 'Close' && history['Open Tabs'].includes(soft) && !history['Recently Closed'].includes(soft)) {
            history['Recently Closed'].push(soft);
            let idx = history['Open Tabs'].indexOf(soft);
            history['Open Tabs'].splice(idx, 1);
            history['Browser Logs'].push(element);
        } else if (action === 'Clear') {
            Object.keys(history).forEach(key => {
                if (key !== "Browser Name") {
                    history[key] = [];
                }
            })
        }
    });
    console.log(history["Browser Name"]);
    console.log(`Open Tabs: ${history["Open Tabs"].join(', ')}`);
    console.log(`Recently Closed: ${history["Recently Closed"].join(', ')}`);
    console.log(`Browser Logs: ${history["Browser Logs"].join(', ')}`);
}

// browserHistory(
//     {
//         "Browser Name": "Mozilla Firefox",
//         "Open Tabs": ["YouTube"],
//         "Recently Closed": ["Gmail", "Dropbox"],
//         "Browser Logs": ["Open Gmail", "Close Gmail", "Open Dropbox", "Open YouTube", "Close Dropbox"]
//     },
//     ["Open Wikipedia", "Clear History and Cache", "Open Twitter"]
// )