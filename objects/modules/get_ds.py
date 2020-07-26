from kubernetes import client, config
from kubernetes.client.rest import ApiException

config.load_kube_config()
apps = client.AppsV1Api()

class K8sDaemonSet:
    def get_damemonsets(ns):           
        try:
            print ("\n[INFO] Fetching dameonsets data...")
            if ns != 'all': 
                namespace = ns
                damemonsets = apps.list_namespaced_daemon_set(namespace, timeout_seconds=10)
            else:             
                damemonsets = apps.list_daemon_set_for_all_namespaces(timeout_seconds=10)
            return damemonsets
        except ApiException as e:
            print("Exception when calling AppsV1Api->list_namespaced_daemon_set: %s\n" % e)