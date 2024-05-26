import { useEffect, useState } from "react";

export const useDebounce = <T>(value: T, delay = 300) => {
    const [debounceValue, setDebounceValue] = useState<T>(value);
    
    useEffect(() => {
        const handler = setTimeout(() => {
            setDebounceValue(value);
        }, delay);
        return () => {
            clearTimeout(handler);
        }
    }, [value, delay])
    
    return debounceValue
}