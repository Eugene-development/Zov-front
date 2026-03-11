export type ToastType = 'success' | 'error' | 'info';

export interface ToastMessage {
	id: string;
	title?: string;
	message: string;
	type: ToastType;
	duration?: number;
}

class ToastState {
	items = $state<ToastMessage[]>([]);

	add(toast: Omit<ToastMessage, 'id'>) {
		const id = crypto.randomUUID();
		const duration = toast.duration ?? 5000;
		const newToast = { ...toast, id, duration };
		this.items.push(newToast);

		if (duration > 0) {
			setTimeout(() => {
				this.remove(id);
			}, duration);
		}
	}

	remove(id: string) {
		this.items = this.items.filter((t) => t.id !== id);
	}
}

export const toastState = new ToastState();
