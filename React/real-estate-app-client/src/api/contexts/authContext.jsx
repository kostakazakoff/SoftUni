/* eslint-disable react/prop-types */
import { createContext } from "react";
import { useEffect, useState } from "react";
import api from "../helpers/Api";

const AuthContext = createContext();

AuthContext.displayName = 'AuthContext';

export const AuthProvider = ({ children }) => {
    const [credentials, setCredentials] = useState({});

    useEffect(() => {
        localStorage.setItem('credentials', JSON.stringify(credentials));
    }, [credentials]);

    useEffect(() => {
        const savedCredentials = JSON.parse(localStorage.getItem('credentials'));
        if (savedCredentials !== null) {
            setCredentials(state => ({ ...state, ...savedCredentials }));
        }
    }, []);

    useEffect(() => {
        if (credentials.isAuthenticated) {
            api.get('user')
                .then(result => console.log('Current USER', result));
        }

        console.log('Not authenticated');
    }, []);

    console.log('Logged in: ', credentials.email);

    const values = {
        user_id: credentials.id,
        email: credentials.email,
        jwt: credentials.jwt,
        isAuthenticated: !!credentials.jwt,
        setCredentials: setCredentials,
    }

    return (
        <AuthContext.Provider value={values}>
            {children}
        </AuthContext.Provider >
    )
}

export default AuthContext;