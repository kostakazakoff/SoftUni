/* eslint-disable react/prop-types */
import { createContext } from "react";
import { useEffect } from "react";
import api from "../helpers/Api";
import usePersistedState from "../hooks/usePersistedState";

const AuthContext = createContext();

AuthContext.displayName = 'AuthContext';

export const AuthProvider = ({ children }) => {
    const [credentials, setCredentials] = usePersistedState('auth', {});

    console.log('Logged in: ', credentials.email);

    const userProps = {
        user_id: credentials.id,
        email: credentials.email,
        jwt: credentials.jwt,
        isAuthenticated: !!credentials.jwt,
        setCredentials: setCredentials,
    }

    return (
        <AuthContext.Provider value={userProps}>
            {children}
        </AuthContext.Provider >
    )
}

export default AuthContext;