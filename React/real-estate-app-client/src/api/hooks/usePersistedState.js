import { useState } from "react";


export default function usePersistedState(key, defaultState) {

    const [state, setState] = useState(() => {
        const persistedState = localStorage.getItem(key);
        
        if (persistedState) {
            return JSON.parse(persistedState);
        }

        return defaultState;
    });


    const setPersistedState = (value) => { // can be value *{}* or function *() => {}*
        setState(value);

        let serializedValue;

        typeof value === "function"
        ? serializedValue = JSON.stringify(value(state))
        : serializedValue = JSON.stringify(value);

        localStorage.setItem(key, serializedValue);
    }

    return [state, setPersistedState];
}