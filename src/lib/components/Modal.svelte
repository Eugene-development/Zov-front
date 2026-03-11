<script lang="ts">
	import { fade, fly } from 'svelte/transition';
	import { backOut } from 'svelte/easing';
	import type { Snippet } from 'svelte';

	let {
		showModal = $bindable(false),
		title = '',
		children
	}: {
		showModal?: boolean;
		title?: string;
		children?: Snippet;
	} = $props();

	function close() {
		showModal = false;
	}

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === 'Escape') close();
	}
</script>

<svelte:window onkeydown={handleKeydown} />

{#if showModal}
	<!-- Backdrop -->
	<!-- svelte-ignore a11y_click_events_have_key_events -->
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div
		class="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4 backdrop-blur-sm"
		transition:fade={{ duration: 300 }}
		onclick={close}
	>
		<!-- Modal Dialog -->
		<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
		<div
			class="relative w-full max-w-lg overflow-hidden bg-surface p-8 shadow-2xl"
			transition:fly={{ y: 50, duration: 400, easing: backOut }}
			onclick={(e) => e.stopPropagation()}
			role="dialog"
			aria-modal="true"
			tabindex="-1"
		>
			<!-- Close Button -->
			<button
				class="absolute top-4 right-4 flex h-8 w-8 items-center justify-center border border-border-light text-text-muted transition-colors hover:border-text-primary hover:text-text-primary focus:outline-none"
				onclick={close}
				aria-label="Закрыть"
			>
				<svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="1.5"
						d="M6 18L18 6M6 6l12 12"
					/>
				</svg>
			</button>

			{#if title}
				<h3 class="mb-6 text-2xl font-light text-primary" style="font-family: var(--font-heading);">
					{title}
				</h3>
			{/if}

			{@render children?.()}
		</div>
	</div>
{/if}
