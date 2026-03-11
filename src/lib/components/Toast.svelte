<script lang="ts">
	import { fly, fade } from 'svelte/transition';
	import { toastState, type ToastMessage } from '$lib/state/toast.svelte';

	let { toast }: { toast: ToastMessage } = $props();

	function close() {
		toastState.remove(toast.id);
	}

	let iconClass = $derived(
		toast.type === 'success'
			? 'text-green-500'
			: toast.type === 'error'
				? 'text-red-500'
				: 'text-blue-500'
	);
</script>

<div
	class="pointer-events-auto relative flex w-full items-start gap-4 overflow-hidden border border-border-light bg-surface p-4 shadow-elevated"
	transition:fly={{ x: 50, duration: 400 }}
>
	<div class="mt-0.5 flex-shrink-0 {iconClass}">
		{#if toast.type === 'success'}
			<svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
				/>
			</svg>
		{:else if toast.type === 'error'}
			<svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
				/>
			</svg>
		{:else}
			<svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
				/>
			</svg>
		{/if}
	</div>

	<div class="flex-1">
		{#if toast.title}
			<h4 class="text-sm font-medium text-primary">{toast.title}</h4>
		{/if}
		<p class="mt-1 text-xs leading-relaxed text-text-secondary">{toast.message}</p>
	</div>

	<button
		class="ml-4 flex-shrink-0 text-text-muted hover:text-text-primary focus:outline-none"
		onclick={close}
		aria-label="Закрыть уведомление"
	>
		<svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M6 18L18 6M6 6l12 12"
			/>
		</svg>
	</button>

	<!-- Progress bar -->
	<div class="absolute bottom-0 left-0 h-0.5 w-full bg-border-light">
		<div
			class="h-full bg-current {iconClass} origin-left"
			style="animation: shrink {toast.duration}ms linear forwards;"
		></div>
	</div>
</div>

<style>
	@keyframes shrink {
		from {
			transform: scaleX(1);
		}
		to {
			transform: scaleX(0);
		}
	}
</style>
