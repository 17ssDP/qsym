target = [
"/home/dp/qsym-result/qsym/kubernetes/cmd/kubeadm/app/cmd/resultImagesListRunWithCustomConfigPath",
"/home/dp/qsym-result/qsym/kubernetes/cmd/kubeadm/app/util/config/resultLoadInitConfigurationFromFile",
"/home/dp/qsym-result/qsym/kubernetes/cmd/kubeadm/app/util/config/resultLoadJoinConfigurationFromFile",
"/home/dp/qsym-result/qsym/kubernetes/cmd/kubeadm/app/phases/etcd/resultCreateLocalEtcdStaticPodManifestFileWithPatches",
"/home/dp/qsym-result/qsym/kubernetes/cmd/kubelet/app/resultIsValidPriorityClass",
"/home/dp/qsym-result/qsym/kubernetes/cmd/kube-proxy/app/resultLoadConfigFailures",
"/home/dp/qsym-result/qsym/kubernetes/cmd/kube-proxy/app/resultAddressFromDeprecatedFlags",
"/home/dp/qsym-result/qsym/kubernetes/cmd/kube-proxy/app/resultProcessHostnameOverrideFlag",
"/home/dp/qsym-result/qsym/kubernetes/cmd/kube-proxy/app/resultLoadConfig",
"/home/dp/qsym-result/qsym/protobuf/resultBytesPrimitives",
"/home/dp/qsym-result/qsym/protobuf/resultNegativeInt32",
"/home/dp/qsym-result/qsym/protobuf/resultRoundTripProto3",
"/home/dp/qsym-result/qsym/protobuf/resultStringEscaping",
"/home/dp/qsym-result/qsym/protobuf/jsonpb/resultUnmarshaling",
"/home/dp/qsym-result/qsym/protobuf/jsonpb/resultMarshalIllegalTime",
"/home/dp/qsym-result/qsym/protobuf/jsonpb/resultUnmarshalUnsetRequiredFields",
"/home/dp/qsym-result/qsym/protobuf/jsonpb/resultUnmarshalNext",
"/home/dp/qsym-result/qsym/protobuf/jsonpb/resultMarshaling",
"/home/dp/qsym-result/qsym/protobuf/jsonpb/resultMarshalAnyJSONPBMarshaler",
"/home/dp/qsym-result/qsym/etcd/client/v2/resultHTTPClusterClientAutoSyncCancelContext",
"/home/dp/qsym-result/qsym/etcd/client/v2/resultHTTPKeysAPISetError",
"/home/dp/qsym-result/qsym/etcd/client/v2/resultHTTPClusterClientSync",
"/home/dp/qsym-result/qsym/beego/adapter/session/resultMem",
"/home/dp/qsym-result/qsym/beego/adapter/session/redis_sentinel/resultRedisSentinel",
"/home/dp/qsym-result/qsym/beego/task/resultParse",
"/home/dp/qsym-result/qsym/beego/task/resultCrudTask",
"/home/dp/qsym-result/qsym/beego/server/web/resultParseForm",
"/home/dp/qsym-result/qsym/beego/core/validation/resultSkipValid",
"/home/dp/qsym-result/qsym/beego/core/validation/resultCanSkipAlso",
"/home/dp/qsym-result/qsym/beego/core/validation/resultPointer",
"/home/dp/qsym-result/qsym/beego/core/utils/resultMail",
"/home/dp/qsym-result/qsym/go-restful/resultRouteBuilder_PathParameter",
"/home/dp/qsym-result/qsym/go-restful/resultTemplateToRegularExpression"
]

for i in target:
    print("/home/dp/qsym-area/qsym/bin/run_qsym_fuzzer.py -a " + i + " -o " + i + " -n qsym -t ** -- ** @@")