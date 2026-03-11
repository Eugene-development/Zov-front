<script lang="ts">
	import { toastState } from '$lib/state/toast.svelte';
	import Toast from '$lib/components/Toast.svelte';
	import { flip } from 'svelte/animate';
</script>

<div
	class="pointer-events-none fixed top-16 right-0 z-[100] flex w-full max-w-sm flex-col gap-2 p-4 sm:top-20 sm:p-6"
>
	{#each toastState.items as toast (toast.id)}
		<div animate:flip={{ duration: 300 }}>
			<Toast {toast} />
		</div>
	{/each}
</div>
