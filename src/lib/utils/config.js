/**
 * Runtime configuration helper for ZOV Frontend
 *
 * In Docker production: reads from window.__APP_CONFIG__ (injected by entrypoint.sh)
 * In development / build-time: falls back to import.meta.env.VITE_* variables
 */

/**
 * @returns {string} Auth API base URL (e.g. https://auth.zov.top/api)
 */
export function getAuthApiUrl() {
	if (typeof window !== 'undefined' && window.__APP_CONFIG__?.AUTH_API_URL) {
		return window.__APP_CONFIG__.AUTH_API_URL + '/api';
	}
	return import.meta.env.VITE_AUTH_API_URL || 'http://localhost:8000/api';
}

/**
 * @returns {string} API Base URL (e.g. https://crud.zov.top/api)
 */
export function getApiBaseUrl() {
	if (typeof window !== 'undefined' && window.__APP_CONFIG__?.API_BASE_URL) {
		return window.__APP_CONFIG__.API_BASE_URL;
	}
	return import.meta.env.VITE_API_BASE_URL || 'http://localhost:8001/api';
}
