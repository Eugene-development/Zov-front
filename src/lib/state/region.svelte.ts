export class RegionState {
	selectedCity = $state<string>('Москва и МО');
	hasConfirmedCity = $state<boolean>(false);
	isCityModalOpen = $state<boolean>(false);

	init() {
		if (typeof window !== 'undefined') {
			const savedCity = localStorage.getItem('zov_selected_city');
			if (savedCity) {
				if (savedCity === 'Москва') {
					this.selectedCity = 'Москва и МО';
					localStorage.setItem('zov_selected_city', 'Москва и МО');
				} else {
					this.selectedCity = savedCity;
				}
			}
			const confirmed = sessionStorage.getItem('zov_bot_filter_confirmed');
			if (confirmed === 'true') {
				this.hasConfirmedCity = true;
			}
		}
	}

	setCity(city: string) {
		this.selectedCity = city;
		if (typeof window !== 'undefined') {
			localStorage.setItem('zov_selected_city', city);
		}
	}

	confirmCity() {
		this.hasConfirmedCity = true;
		if (typeof window !== 'undefined') {
			sessionStorage.setItem('zov_bot_filter_confirmed', 'true');
		}
	}
}

export const regionState = new RegionState();
if (typeof window !== 'undefined') {
	regionState.init();
}
